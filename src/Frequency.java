import java.util.Enumeration;
import java.util.Vector;

class Frequency {
  double value;
  
  private Vector vectors = new Vector();
  
  void addVector(Vector3d paramVector3d) { this.vectors.addElement(paramVector3d); }
  
  Vector3d getVector(int paramInt) { return (Vector3d)this.vectors.elementAt(paramInt); }
  
  int getNumberVectors() { return this.vectors.size(); }
  
  Enumeration getVectors() { return this.vectors.elements(); }
  
  void removeVectors() { this.vectors.removeAllElements(); }
}


/* Location:              /home/xyz666/gausspy/Xvibs/xvibs.jar!/Frequency.class
 * Java compiler version: 2 (46.0)
 * JD-Core Version:       1.0.7
 */