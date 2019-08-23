import java.io.BufferedReader;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Hashtable;
import java.util.StringTokenizer;
import java.util.Vector;

class DaltonReader implements MoleculeReader {
  static final double angstromPerBohr = 0.529177249D;
  
  BufferedReader input;
  
  Hashtable atomTypeMap = new Hashtable();
  
  public DaltonReader(Reader paramReader) { this.input = new BufferedReader(paramReader); }
  
  public void read(Molecule paramMolecule) throws Exception {
    while (this.input.ready()) {
      String str = this.input.readLine();
      if (str.trim().startsWith("Total energy")) {
        paramMolecule.energy = toEnergy(str);
        continue;
      } 
      if (str.trim().startsWith("Atoms and basis sets")) {
        readAtomTypes();
        continue;
      } 
      if (str.trim().startsWith("Molecular geometry")) {
        readCoordinates(paramMolecule);
        continue;
      } 
      if (str.trim().startsWith("Normal Coordinates")) {
        readFrequencies(paramMolecule);
        break;
      } 
    } 
  }
  
  double toEnergy(String paramString) throws Exception {
    double d = 0.0D;
    StringReader stringReader = new StringReader(paramString);
    StreamTokenizer streamTokenizer = new StreamTokenizer(stringReader);
    while (streamTokenizer.nextToken() != -1) {
      if (streamTokenizer.ttype == -2) {
        d = streamTokenizer.nval;
        break;
      } 
    } 
    if (streamTokenizer.ttype == -1)
      throw new Exception("Error reading energy"); 
    return d;
  }
  
  void readAtomTypes() throws Exception {
    this.atomTypeMap.clear();
    for (byte b = 0; b < 9; b++)
      String str = this.input.readLine(); 
    while (this.input.ready()) {
      String str1 = this.input.readLine().trim();
      if (str1.startsWith("-----"))
        break; 
      StringTokenizer stringTokenizer = new StringTokenizer(str1);
      if (stringTokenizer.countTokens() < 3)
        throw new Exception("Error reading atom types"); 
      String str2 = stringTokenizer.nextToken();
      stringTokenizer.nextToken();
      Integer integer = new Integer(stringTokenizer.nextToken());
      this.atomTypeMap.put(str2, integer);
    } 
  }
  
  void readCoordinates(Molecule paramMolecule) throws Exception {
    paramMolecule.removeAtoms();
    String str = this.input.readLine();
    str = this.input.readLine();
    while (this.input.ready()) {
      str = this.input.readLine().trim();
      if (str.length() == 0)
        break; 
      Atom atom = new Atom();
      StringTokenizer stringTokenizer = new StringTokenizer(str);
      if (stringTokenizer.countTokens() < 3)
        throw new Exception("Error reading coordinates"); 
      String str1 = stringTokenizer.nextToken();
      if (this.atomTypeMap.containsKey(str1)) {
        atom.atomicNumber = ((Integer)this.atomTypeMap.get(str1)).intValue();
      } else {
        atom.atomicNumber = -1;
      } 
      atom.position = new Point3d();
      atom.position.x = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D;
      atom.position.y = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D;
      atom.position.z = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D;
      paramMolecule.addAtom(atom);
    } 
  }
  
  void readFrequencies(Molecule paramMolecule) throws Exception {
    paramMolecule.removeFrequencies();
    String str = this.input.readLine();
    str = this.input.readLine();
    for (str = this.input.readLine(); this.input.ready(); str = this.input.readLine()) {
      String str1 = this.input.readLine().trim();
      str = this.input.readLine().trim();
      if (!str.startsWith("-----"))
        break; 
      Vector vector = new Vector();
      StringTokenizer stringTokenizer = new StringTokenizer(str1);
      int i = stringTokenizer.countTokens() / 2;
      for (byte b1 = 0; b1 < i; b1++) {
        stringTokenizer.nextToken();
        Frequency frequency = new Frequency();
        String str2 = stringTokenizer.nextToken();
        frequency.value = (new Double(str2)).doubleValue();
        vector.addElement(frequency);
      } 
      Vector3d[] arrayOfVector3d = new Vector3d[vector.size()];
      str = this.input.readLine();
      byte b2;
      for (b2 = 0; b2 < paramMolecule.getNumberAtoms(); b2++) {
        str = this.input.readLine();
        stringTokenizer = new StringTokenizer(str);
        stringTokenizer.nextToken();
        stringTokenizer.nextToken();
        byte b;
        for (b = 0; b < vector.size(); b++) {
          arrayOfVector3d[b] = new Vector3d();
          (arrayOfVector3d[b]).x = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D;
        } 
        str = this.input.readLine();
        stringTokenizer = new StringTokenizer(str);
        stringTokenizer.nextToken();
        stringTokenizer.nextToken();
        for (b = 0; b < vector.size(); b++)
          (arrayOfVector3d[b]).y = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D; 
        str = this.input.readLine();
        stringTokenizer = new StringTokenizer(str);
        stringTokenizer.nextToken();
        stringTokenizer.nextToken();
        for (b = 0; b < vector.size(); b++) {
          (arrayOfVector3d[b]).z = (new Double(stringTokenizer.nextToken())).doubleValue() * 0.529177249D;
          ((Frequency)vector.elementAt(b)).addVector(arrayOfVector3d[b]);
        } 
        str = this.input.readLine();
      } 
      for (b2 = 0; b2 < vector.size(); b2++)
        paramMolecule.addFrequency((Frequency)vector.elementAt(b2)); 
    } 
  }
}


/* Location:              /home/xyz666/gausspy/Xvibs/xvibs.jar!/DaltonReader.class
 * Java compiler version: 2 (46.0)
 * JD-Core Version:       1.0.7
 */