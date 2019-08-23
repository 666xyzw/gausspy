class Tuple3d {
  double x;
  
  double y;
  
  double z;
  
  Tuple3d() {}
  
  Tuple3d(double paramDouble1, double paramDouble2, double paramDouble3) {
    this.x = paramDouble1;
    this.y = paramDouble2;
    this.z = paramDouble3;
  }
  
  Tuple3d(Tuple3d paramTuple3d) {
    this.x = paramTuple3d.x;
    this.y = paramTuple3d.y;
    this.z = paramTuple3d.z;
  }
  
  void add(Tuple3d paramTuple3d) {
    this.x += paramTuple3d.x;
    this.y += paramTuple3d.y;
    this.z += paramTuple3d.z;
  }
  
  void scale(double paramDouble) {
    this.x *= paramDouble;
    this.y *= paramDouble;
    this.z *= paramDouble;
  }
}


/* Location:              /home/xyz666/gausspy/Xvibs/xvibs.jar!/Tuple3d.class
 * Java compiler version: 2 (46.0)
 * JD-Core Version:       1.0.7
 */