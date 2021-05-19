const getListStudentIds = (list) => {
  if (Array.isArray(list)) {
    const ids = [];
    list.forEach(({ id }) => ids.push(id));
    return ids;
  }
  return [];
};

export default getListStudentIds;
