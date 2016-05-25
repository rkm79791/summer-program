import numpy as np
import sys
sys.path.insert(0,'../../extra-files')
import masses

class Molecule(object):
    """
    Python class used to store the geometry, masses, and nuclear charges of a molecule
    """

    def __init__(self, geom):
        """
        Creates a molecule with a geometry and corresponding units
        """

        lines = geom.strip().split("\n")

        units = lines[1]
        
        natom = int(lines[0])

        atoms = []
        geom = []

        for line in lines[2:]:
            atom, x, y, z = line.split()
            atoms.append(atom)
            geom.append([float(x), float(y), float(z)])

        self.units = units
        self.natom = natom
        self.atoms = atoms
        self.geom = np.array(geom)

        mass = []
        charges =[]

        for atom in atoms:
            mass.append(float(masses.get_mass(atom)))
            charges.append(int(masses.get_charge(atom))) #might want to include symbols

        self.mass = mass
        self.charges = charges

    def to_bohr(self):
        """
        Converts geometry to Bohr
        """

        if self.units == "Angstrom":
            self.units = "Bohr"
            self.geom *= 1.889725989
    
    def to_angstrom(self):
        """
        Converts geometry to Angstroms
        """

        if self.units == "Bohr":
            self.units = "Angstrom"
            self.geom /= 1.889725989

    def __len__(self):
        """
        Returns the length of the molecule
        """
        return self.natom

    def __repr__(self):
        return "{:d}\n".format(self.natom) + self.__str__()

    def __str__(self):
        
        """
        Format the molecule in a nice way
        """
        line_form = "{:2s} {: >15.10f} {: >15.10f} {: >15.10f}\n"
        out = "units {:s}\n".format(self.units)
        for atom, (x, y, z) in zip(self.atoms, self.geom):
            out += line_form.format(atom, x, y, z)
        return out

    def copy(self):
        return Molecule(self.__repr__(), self.units)

if __name__ == "__main__":
    geom = open("../../extra-files/molecule.xyz").read()
    mol = Molecule(geom)
    print(mol)
