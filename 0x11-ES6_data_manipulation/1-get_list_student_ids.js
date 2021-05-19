const getListStudentIds = (array) => {
  if (Array.isArray(array)) return array.map((x) => x.id);
  return [];
};

export default getListStudentIds;
