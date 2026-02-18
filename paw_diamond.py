{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "efed1cb9-5b6c-48bd-a368-5caf74db258a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter number of vertices:\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter adjacency matrix row by row (space-separated 0/1):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 0 1 0 0 1 1\n",
      " 1 0 1 0 0 0\n",
      " 0 1 0 1 0 0\n",
      " 0 0 1 0 1 1\n",
      " 1 0 0 1 0 0\n",
      " 1 0 0 1 0 0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No paw found in G.\n",
      "No diamond found in G.\n",
      "Co-paw found in G (paw in complement) on vertices: (0, 2, 4, 5)\n",
      "Co-paw found in G (paw in complement) on vertices: (1, 3, 4, 5)\n",
      "No co-diamond found in G.\n"
     ]
    }
   ],
   "source": [
    "import itertools\n",
    "\n",
    "def is_paw(adj, vertices):\n",
    "    degrees = [sum(adj[v][u] for u in vertices if u != v) for v in vertices]\n",
    "    if sorted(degrees) != [1,2,2,3]:\n",
    "        return False\n",
    "    triangle_candidates = [vertices[i] for i in range(4) if degrees[i] >= 2]\n",
    "    if len(triangle_candidates) != 3:\n",
    "        return False\n",
    "    a, b, c = triangle_candidates\n",
    "    return adj[a][b] and adj[a][c] and adj[b][c]\n",
    "\n",
    "def is_diamond(adj, vertices):\n",
    "    edge_count = sum(adj[i][j] for i in range(4) for j in range(i+1,4))\n",
    "    if edge_count != 5:\n",
    "        return False\n",
    "    degrees = [sum(adj[v][u] for u in vertices if u != v) for v in vertices]\n",
    "    return min(degrees) >= 1\n",
    "\n",
    "def find_forbidden(adj):\n",
    "    \"\"\"\n",
    "    Returns four lists:\n",
    "    paws, diamonds, co-paws, co-diamonds\n",
    "    Each list contains tuples of the vertices forming that forbidden subgraph.\n",
    "    \"\"\"\n",
    "    n = len(adj)\n",
    "    paws = []\n",
    "    diamonds = []\n",
    "\n",
    "    for vertices in itertools.combinations(range(n), 4):\n",
    "        if is_paw(adj, vertices):\n",
    "            paws.append(vertices)\n",
    "        elif is_diamond(adj, vertices):\n",
    "            diamonds.append(vertices)\n",
    "\n",
    "    # check in complement\n",
    "    adj_comp = complement_matrix(adj)\n",
    "    co_paws = []\n",
    "    co_diamonds = []\n",
    "    for vertices in itertools.combinations(range(n), 4):\n",
    "        if is_paw(adj_comp, vertices):\n",
    "            co_paws.append(vertices)\n",
    "        elif is_diamond(adj_comp, vertices):\n",
    "            co_diamonds.append(vertices)\n",
    "\n",
    "    return paws, diamonds, co_paws, co_diamonds\n",
    "\n",
    "def complement_matrix(adj):\n",
    "    n = len(adj)\n",
    "    comp = [[0]*n for _ in range(n)]\n",
    "    for i in range(n):\n",
    "        for j in range(n):\n",
    "            if i != j:\n",
    "                comp[i][j] = 1 - adj[i][j]\n",
    "    return comp\n",
    "\n",
    "# ===== INPUT =====\n",
    "print(\"Enter number of vertices:\")\n",
    "n = int(input())\n",
    "print(\"Enter adjacency matrix row by row (space-separated 0/1):\")\n",
    "adj = [list(map(int, input().split())) for _ in range(n)]\n",
    "\n",
    "# ===== CHECK =====\n",
    "paws, diamonds, co_paws, co_diamonds = find_forbidden(adj)\n",
    "\n",
    "if paws:\n",
    "    for verts in paws:\n",
    "        print(\"Paw found in G on vertices:\", verts)\n",
    "else:\n",
    "    print(\"No paw found in G.\")\n",
    "\n",
    "if diamonds:\n",
    "    for verts in diamonds:\n",
    "        print(\"Diamond found in G on vertices:\", verts)\n",
    "else:\n",
    "    print(\"No diamond found in G.\")\n",
    "\n",
    "if co_paws:\n",
    "    for verts in co_paws:\n",
    "        print(\"Co-paw found in G (paw in complement) on vertices:\", verts)\n",
    "else:\n",
    "    print(\"No co-paw found in G.\")\n",
    "\n",
    "if co_diamonds:\n",
    "    for verts in co_diamonds:\n",
    "        print(\"Co-diamond found in G (diamond in complement) on vertices:\", verts)\n",
    "else:\n",
    "    print(\"No co-diamond found in G.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "533b2545-34ea-4898-8111-c175ad14f46f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
