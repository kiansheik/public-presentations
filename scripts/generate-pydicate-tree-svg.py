#!/usr/bin/env python3
"""Generate a Slidev-ready SVG tree from an oldtupicorpus pydicate expression."""

from __future__ import annotations

import argparse
import html
import importlib.util
import math
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OLDTUPI_ROOT = REPO_ROOT.parent / "oldtupicorpus"
DEFAULT_SOURCE = "araujo_catecismo_1686"
DEFAULT_OUTPUT = (
    REPO_ROOT
    / "public/assets/enapol-2026-executable-grammar/araujo-line-tree.svg"
)


@dataclass
class TreeNode:
    label: str
    category: str
    relation: str
    base: str
    surface: str
    node_class: str
    children: list["TreeNode"] = field(default_factory=list)
    x: float = 0
    y: float = 0


def load_expression(oldtupi_root: Path, source: str, index: int):
    sys.path.insert(0, str(oldtupi_root))
    source_path = oldtupi_root / "historic" / source
    if source_path.suffix != ".py":
        source_path = oldtupi_root / "historic" / f"{source}.tu.py"
    if not source_path.exists():
        raise FileNotFoundError(f"Historic source not found: {source_path}")

    module_name = f"_enapol_{source_path.name.replace('.', '_')}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load {source_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    collection = getattr(module, source_path.name.removesuffix(".tu.py"), None)
    if collection is None:
        collection = getattr(module, source_path.stem, None)
    if collection is None:
        collection = getattr(module, "l", None)
    if collection is None:
        lists = [v for v in vars(module).values() if isinstance(v, list)]
        if len(lists) == 1:
            collection = lists[0]
    if collection is None:
        raise ValueError(f"No expression list found in {source_path}")

    try:
        return collection[index]
    except IndexError as exc:
        raise IndexError(f"Index {index} out of range for {source_path}") from exc


def node_kind(category: str, relation: str, children: list[TreeNode]) -> str:
    if relation == "root":
        return "root"
    if category == "postposition":
        return "postposition"
    if category in {"deverbal_noun", "deadverbal_noun"}:
        return "derived"
    if children:
        return "internal"
    return "leaf"


def relation_label(kind: str, index: int | None = None) -> str:
    if kind == "arg":
        return f"argument {index}" if index is not None else "argument"
    if kind == "pre":
        return "pre-adjunct"
    if kind == "post":
        return "post-adjunct"
    if kind == "vpre":
        return "verbal pre-adjunct"
    if kind == "vpost":
        return "verbal adjunct"
    if kind == "composition":
        return "composition"
    return kind


def strip_for_core(pred):
    stripped = pred.copy()
    stripped.pre_adjuncts = []
    stripped.post_adjuncts = []
    stripped.v_adjuncts = []
    stripped.v_adjuncts_pre = []
    stripped.principal = None
    return stripped


def build_tree(pred, relation: str = "root") -> TreeNode:
    children: list[TreeNode] = []
    for idx, arg in enumerate(getattr(pred, "arguments", []) or [], start=1):
        children.append(build_tree(arg, relation_label("arg", idx)))
    for adj in getattr(pred, "pre_adjuncts", []) or []:
        children.append(build_tree(adj, relation_label("pre")))
    for adj in getattr(pred, "post_adjuncts", []) or []:
        children.append(build_tree(adj, relation_label("post")))
    for adj in getattr(pred, "v_adjuncts_pre", []) or []:
        children.append(build_tree(adj, relation_label("vpre")))
    for adj in getattr(pred, "v_adjuncts", []) or []:
        children.append(build_tree(adj, relation_label("vpost")))
    for comp in getattr(pred, "compositions", []) or []:
        children.append(build_tree(comp, relation_label("composition")))

    category = getattr(pred, "category", pred.__class__.__name__)
    base = getattr(pred, "verbete", "?")
    surface = pred.eval() if hasattr(pred, "eval") else str(pred)
    try:
        core_surface = strip_for_core(pred).eval()
    except Exception:
        core_surface = surface

    display_surface = surface if surface != base else core_surface
    label = base if display_surface == base else f"{base} → {display_surface}"
    return TreeNode(
        label=label,
        category=category,
        relation=relation,
        base=base,
        surface=surface,
        node_class=node_kind(category, relation, children),
        children=children,
    )


def leaves(node: TreeNode) -> list[TreeNode]:
    if not node.children:
        return [node]
    out: list[TreeNode] = []
    for child in node.children:
        out.extend(leaves(child))
    return out


def assign_positions(root: TreeNode, width: int, top: int, level_gap: int) -> int:
    leaf_nodes = leaves(root)
    margin = 80
    if len(leaf_nodes) == 1:
        leaf_nodes[0].x = width / 2
    else:
        step = (width - margin * 2) / (len(leaf_nodes) - 1)
        for i, node in enumerate(leaf_nodes):
            node.x = margin + step * i

    max_depth = 0

    def place(node: TreeNode, depth: int) -> None:
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for child in node.children:
            place(child, depth + 1)
        if node.children:
            node.x = sum(child.x for child in node.children) / len(node.children)
        node.y = top + depth * level_gap

    place(root, 0)
    return max_depth


def wrap_label(text: str, width: int = 22, max_lines: int = 3) -> list[str]:
    lines = []
    for chunk in text.split(" → "):
        wrapped = textwrap.wrap(chunk, width=width, break_long_words=False) or [chunk]
        lines.extend(wrapped)
        if chunk != text.split(" → ")[-1]:
            lines[-1] += " →"
    if len(lines) > max_lines:
        return lines[: max_lines - 1] + [lines[max_lines - 1] + "..."]
    return lines


def svg_text(lines: list[str], x: float, y: float, css_class: str, line_height: int = 18) -> str:
    escaped = [html.escape(line) for line in lines]
    start = y - ((len(escaped) - 1) * line_height) / 2
    tspans = [
        f'<tspan x="{x:.1f}" y="{start + i * line_height:.1f}">{line}</tspan>'
        for i, line in enumerate(escaped)
    ]
    return f'<text class="{css_class}" text-anchor="middle">{"".join(tspans)}</text>'


def node_rect(node: TreeNode) -> str:
    width = 180 if node.node_class != "root" else 320
    height = 82 if node.node_class != "root" else 90
    if node.node_class == "leaf":
        width = 150
    x = node.x - width / 2
    y = node.y - height / 2
    label_lines = wrap_label(node.label, width=24 if width >= 180 else 18)
    category = node.category.replace("_", " ")
    rel = node.relation
    return "\n".join(
        [
            f'<g class="node node-{node.node_class}">',
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{width}" height="{height}" rx="7"/>',
            svg_text([rel.upper()], node.x, y + 18, "rel", 0),
            svg_text(label_lines, node.x, y + height / 2 + 7, "label"),
            svg_text([category], node.x, y + height - 13, "category", 0),
            "</g>",
        ]
    )


def edge_path(parent: TreeNode, child: TreeNode) -> str:
    color_class = "edge-post" if child.node_class == "postposition" else "edge"
    return (
        f'<path class="{color_class}" d="M {parent.x:.1f} {parent.y + 45:.1f} '
        f'C {parent.x:.1f} {parent.y + 78:.1f}, {child.x:.1f} {child.y - 78:.1f}, '
        f'{child.x:.1f} {child.y - 45:.1f}"/>'
    )


def walk_nodes(node: TreeNode) -> list[TreeNode]:
    out = [node]
    for child in node.children:
        out.extend(walk_nodes(child))
    return out


def render_svg(expr, root: TreeNode) -> str:
    width = 1180
    level_gap = 126
    max_depth = assign_positions(root, width=width, top=150, level_gap=level_gap)
    height = max(720, 150 + max_depth * level_gap + 120)
    surface = html.escape(expr.eval())
    annotated_note = (
        "árvore gerada do objeto pydicate; rótulos e relações vêm "
        "dos atributos estruturais usados pela gramática"
    )

    edge_markup = []
    for node in walk_nodes(root):
        for child in node.children:
            edge_markup.append(edge_path(node, child))

    nodes = "\n".join(node_rect(node) for node in walk_nodes(root))

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Árvore pydicate gerada para a linha de Araújo</title>
  <desc id="desc">Árvore gerada a partir do objeto pydicate que avalia para: {surface}</desc>
  <defs>
    <style>
      .bg{{fill:#fffaf0}}
      .subtitle{{font:600 16px Arial,sans-serif;fill:#6b6257}}
      .surface{{font:700 28px Georgia,serif;fill:#1f2421}}
      .annotated{{font:600 11px Menlo,Consolas,monospace;fill:#6b6257}}
      .edge,.edge-post{{fill:none;stroke:#6f5b35;stroke-width:2.5}}
      .edge-post{{stroke:#4f8a82}}
      .node rect{{fill:#f7f1e6;stroke:#6f5b35;stroke-width:2.2}}
      .node-root rect{{fill:#f7e6de;stroke:#a5432d}}
      .node-derived rect{{fill:#f7e6de;stroke:#a5432d}}
      .node-postposition rect{{fill:#ecf4ef;stroke:#4f8a82}}
      .rel{{font:700 12px Arial,sans-serif;fill:#a5432d}}
      .label{{font:700 16px Menlo,Consolas,monospace;fill:#1f2421}}
      .category{{font:600 12px Arial,sans-serif;fill:#6b6257}}
    </style>
  </defs>
  <rect class="bg" width="{width}" height="{height}"/>
  <text x="{width / 2}" y="42" text-anchor="middle" class="surface">{surface}</text>
  <text x="{width / 2}" y="68" text-anchor="middle" class="subtitle">gerado de oldtupicorpus/historic/araujo_catecismo_1686.tu.py · índice 6</text>
  <text x="{width / 2}" y="{height - 30}" text-anchor="middle" class="annotated">{html.escape(annotated_note)}</text>
  {"".join(edge_markup)}
  {nodes}
</svg>
'''


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oldtupi-root", type=Path, default=DEFAULT_OLDTUPI_ROOT)
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--index", type=int, default=6)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    expr = load_expression(args.oldtupi_root.resolve(), args.source, args.index)
    tree = build_tree(expr)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render_svg(expr, tree), encoding="utf-8")
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
