export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a number');
    if (!Array.isArray(students)) throw TypeError('Stundents must be an array of Strings');
    if (students.every((est) => typeof est !== 'string')) throw TypeError('Stundents must be an array of Strings');

    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(newName) {
    if (typeof newName !== 'string') throw TypeError('Name must be a string');
    this._name = newName;
  }

  get length() {
    return this._length;
  }

  set length(newLength) {
    if (typeof newLength !== 'number') throw TypeError('Length must be a number');
    this._length = newLength;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) throw TypeError('Stundents must be an iarray of Strings');
    if (newStudents.every((est) => typeof est !== 'string')) throw TypeError('Stundents must be an array of Strings');
    this._students = newStudents;
  }
}
