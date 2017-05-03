package workspace.ws.ds.algos.misc;

import junit.framework.TestCase;

public class ExcelColumnsTest extends TestCase {

	public void testExcelCol() {
		assertEquals(ExcelColumns.getColName(26), "Z");
		assertEquals(ExcelColumns.getColName(51), "AY");
		assertEquals(ExcelColumns.getColName(52), "AZ");
		assertEquals(ExcelColumns.getColName(705), "AAC");
	}

}
