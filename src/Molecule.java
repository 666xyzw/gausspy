import java.util.Enumeration;
import java.util.Vector;

class Molecule {
  double energy;
  
  private Vector atoms = new Vector();
  
  private Vector frequencies = new Vector();
  
  void addAtom(Atom paramAtom) { this.atoms.addElement(paramAtom); }
  
  Atom getAtom(int paramInt) { return (Atom)this.atoms.elementAt(paramInt); }
  
  int getNumberAtoms() { return this.atoms.size(); }
  
  Enumeration getAtoms() { return this.atoms.elements(); }
  
  void removeAtoms() { this.atoms.removeAllElements(); }
  
  void addFrequency(Frequency paramFrequency) { this.frequencies.addElement(paramFrequency); }
  
  Frequency getFrequency(int paramInt) { return (Frequency)this.frequencies.elementAt(paramInt); }
  
  int getNumberFrequencies() { return this.frequencies.size(); }
  
  Enumeration getFrequencies() { return this.frequencies.elements(); }
  
  void removeFrequencies() { this.frequencies.removeAllElements(); }
  
  void removeFrequency(int paramInt) { this.frequencies.removeElementAt(paramInt); }
  
  Vector vibration(int paramInt1, int paramInt2, double paramDouble, boolean paramBoolean) {
    Vector vector = new Vector(paramInt2);
    Frequency frequency = (Frequency)this.frequencies.elementAt(paramInt1);
    for (byte b = 0; b < paramInt2; b++) {
      double d;
      Molecule molecule = new Molecule();
      molecule.energy = this.energy;
      if (paramBoolean) {
        d = paramDouble * Math.cos(Math.PI * b / (paramInt2 - 1));
      } else {
        d = paramDouble * Math.sin(6.283185307179586D * b / paramInt2);
      } 
      for (byte b1 = 0; b1 < this.atoms.size(); b1++) {
        Atom atom1 = new Atom();
        Atom atom2 = (Atom)this.atoms.elementAt(b1);
        atom1.atomicNumber = atom2.atomicNumber;
        Tuple3d tuple3d = new Tuple3d(frequency.getVector(b1));
        tuple3d.scale(d);
        atom1.position = new Point3d(atom2.position);
        atom1.position.add(tuple3d);
        molecule.atoms.addElement(atom1);
      } 
      vector.addElement(molecule);
    } 
    return vector;
  }
}
