/**Load Dynamic Ajax Data to Datatables */
const albumTableBody = document.getElementById("album-table-body");

const handleAlbumsSearch = (elem) => {
  // Wait for 2s Before Request Again
  clearTimeout(timer);
  timer = setTimeout(() => {
    fetchAlbums(`/creator/album-response?q=${elem.value}`);
  }, 1000);
};

const fetchAlbums = async (url) => {
  await getRequest(url, handleAlbumsResponse);
};

const handleAlbumsResponse = (response) => {
  albumTableBody.innerHTML = "";
  response.data.forEach((album) => {
    const tr = `<tr>
                          <td class="p-4 border-b border-slate-200">
                              <div class="flex items-center gap-3">
                                  <img src="${
                                    album.cover_art || "/static/img/empty.png"
                                  }"
                                      alt="${album}"
                                      class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                                  <div class="flex flex-col">
                                      <p class="text-sm font-semibold text-white">
                                          ${album.name}
                                      </p>
                                      <p class="text-sm font-light text-white italic">
                                      ${album.artist} | ${new Date(
      album.release_date
    ).toLocaleDateString({ year: "numeric", month: "long", day: "numeric" })}
                                      </p>
                                  </div>
                              </div>
                          </td>
                          <td class="p-4 border-b border-slate-200">
                              <p class="text-sm font-semibold text-white">
                                  ${album.tracks_count} Songs
                              </p>
                          </td>
                          <td class="p-4 border-b border-slate-200">
                              <p class="text-sm font-semibold text-white">
                                 ${durationReadbleFormat(album.duration)} Tracks
                              </p>
                          </td>
                          <td class="p-4 border-b border-slate-200">
                              <p class="text-sm text-white">
                                  ${album.popularity} Fans
                              </p>
                          </td>
                          <td class="p-4 border-b border-slate-200">
                              <button onclick="albumPlayer(this)" class="btn btn-sm btn-circle btn-success" id="play-album-${
                                album.id
                              }">
                                  <i class="fa fa-play"></i>
                              </button>
                          </td>
                      </tr>`;
    albumTableBody.innerHTML += tr;
  });
};

fetchAlbums(`/creator/album-response/`);
