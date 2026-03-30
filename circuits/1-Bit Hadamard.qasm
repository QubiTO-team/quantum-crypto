OPENQASM 3.0;
include "stdgates.inc";
bit[1] c;
bit[1] meas;
qubit[1] q;
h q[0];
barrier q[0];
meas[0] = measure q[0];
