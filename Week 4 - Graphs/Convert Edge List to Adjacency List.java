/*
This problem gives you an edge list, along with how many nodes there are in
the graph, and asks you to turn it into an adjacency list.
*/

static ArrayList<ArrayList<Integer>> convert_edge_list_to_adjacency_list(Integer n, ArrayList<ArrayList<Integer>> edges) {
      ArrayList<ArrayList<Integer>> list = new ArrayList<>();
      
      // Create N empty array lists
      for (int i = 0; i < n; i++) {
          list.add(new ArrayList<Integer>());
      }
      
      for(ArrayList<Integer> edge : edges) {
          int startNode = edge.get(0);
          int endNode = edge.get(1);
          
          list.get(startNode).add(endNode);
          list.get(endNode).add(startNode);
          
      }
      
      for (int i = 0; i < n; i++) {
          Collections.sort(list.get(i));
      }
      
      return list;
}
