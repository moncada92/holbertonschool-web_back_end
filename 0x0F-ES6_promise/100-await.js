import { uploadPhoto, createUser } from './utils';

async function asyncUploadUser() {
  try {
    const photoData = await uploadPhoto();
    const userData = await createUser();
    return { photo: photoData, user: userData };
  } catch (err) {
    return { photo: null, user: null };
  }
}

export default asyncUploadUser;
