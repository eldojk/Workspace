package workspace.ws.ds.algos.arrays;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

/**
 * http://www.geeksforgeeks.org/design-a-data-structure-that-supports-insert-
 * delete-search-and-getrandom-in-constant-time/
 * 
 * @author joseph
 *
 */
public class CustomDataStructure {
	private List<Integer> list;
	private Map<Integer, Integer> map;

	public CustomDataStructure() {
		list = new ArrayList<Integer>();
		map = new HashMap<Integer, Integer>();
	}

	public void insert(int key) {
		if (map.get(key) != null)
			return;

		int index = list.size();
		list.add(key);
		map.put(key, index);
	}

	/**
	 * Swap the last element with this element in array and remove the last
	 * element. Swapping is done because the last element can be removed in O(1)
	 * time
	 * 
	 * @param key
	 */
	public void delete(int key) {
		Integer index = map.get(key);

		if (index == null)
			return;

		map.remove(key);

		int size = list.size();
		int last = list.get(size - 1);
		Collections.swap(list, index, size - 1);

		list.remove(size - 1);
		map.put(last, index);
	}
	
	public int getRandom() {
		Random random = new Random();
		int index = random.nextInt(list.size());
		
		return list.get(index);
	}
	
	public Integer search(int key) {
		return map.get(key);
	}
}
