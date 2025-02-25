/**Handles Library App Views Scripts */
const handleUserLibraryResponse = (response) => {
  /**Create Toast Only */
  createToast(response.message);
};

const likeAlbum = (elem) => {
  const id = elem.id.split("-")[1];
  postRequest(
    "/library/user-album/",
    { id: id, type: "add_album" },
    handleUserLibraryResponse
  );
};

const unlikeAlbum = (elem) => {
  const id = elem.id.split("-")[1];
  postRequest(
    "/library/user-album/",
    { id: id, type: "remove_album" },
    handleUserLibraryResponse
  );
};
const likeSong = (elem) => {
  const id = elem.id.split("-")[1];
  postRequest(
    "/library/user-album/",
    { id: id, type: "add_song" },
    handleUserLibraryResponse
  );
};

const unlikeSong = (elem) => {
  const id = elem.id.split("-")[1];
  postRequest(
    "/library/user-album/",
    { id: id, type: "remove_song" },
    handleUserLibraryResponse
  );
};
const createToast = (msg) => {
  /**Tailwind & Js Toast */
  toast = document.getElementById("custom-toast");
  toastBody = document.getElementById("toast-body");
  toastBody.innerHTML = msg;
  $(toast).show();
};
