package workspace.ws.ds.algos.misc;

import java.util.HashMap;
import java.util.Map;

import workspace.ws.ds.data.DLLNode;

/**
 * amzn, msft
 * 
 * LRU Cache
 * 
 * @author eldo.joseph
 *
 * @param <Key>
 * @param <Value>
 */
public class LRUCache<Key, Value> {
	
	private int cacheSize;
	private int currentSize;
	
	private DLLNode<Key, Value> head;
	private DLLNode<Key, Value> tail;
	
	private Map<Key, DLLNode<Key, Value>> map;
	
	public LRUCache(int cacheSize) {
		this.cacheSize = cacheSize;
		map = new HashMap<Key, DLLNode<Key, Value>>();
	}
	
	/**
	 * Store in cache
	 * 
	 * @param key
	 * @param value
	 */
	public void put(Key key, Value value) {
		
		if (map.get(key) != null) {
			
			DLLNode<Key, Value> node = map.get(key);
			node.data = value;
			moveToFront(node);
		}
		else {
			
			DLLNode<Key, Value> node = new DLLNode<Key, Value>(key, value);
			map.put(key, node);
			addToFront(node);
		}
		
		if (currentSize > cacheSize) {
			removeLastNode();
		}
	}
	
	/**
	 * Retrieve from cache
	 * 
	 * @param key
	 * @return
	 */
	public Value get(Key key) {
		
		DLLNode<Key, Value> node = map.get(key);
		
		if (node == null)
			return null;
		
		moveToFront(node);
		return node.data;
	}

	private void removeLastNode() {
		
		DLLNode<Key, Value> lastNode = tail;
		
		if (lastNode == null)
			return;
		
		tail = lastNode.prev;
		
		if (tail == null) {
			head = null;
		}
		else {
			tail.next = null;
		}
		
		lastNode.prev = null;
		currentSize--;
	}

	private void addToFront(DLLNode<Key, Value> node) {
		
		if (head == null) {
			head = node;
			tail = head;
		}
		else {
			node.next = head;
			head.prev = node;
			head = node;
		}
		
		currentSize++;
	}

	private void moveToFront(DLLNode<Key, Value> node) {
		DLLNode<Key, Value> prevNode = node.prev;
		DLLNode<Key, Value> nextNode = node.next;
		
		if (prevNode == null)
			return;
		
		prevNode.next = nextNode;
		
		if (nextNode != null)
			nextNode.prev = prevNode;
		
		addToFront(node);
		currentSize--;
	}
}
