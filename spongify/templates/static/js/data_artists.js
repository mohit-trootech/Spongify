/**Load Dynamic Ajax Data to Datatables */
const artistTableBody = document.getElementById("artist-table-body");
let timer = null;

const handleAristSearch = (elem) => {
  // Wait for 2s Before Request Again
  clearTimeout(timer);
  timer = setTimeout(() => {
    fetchArtists(`/creator/artist-response?q=${elem.value}`);
  }, 1000);
};

const fetchArtists = async (url) => {
  await getRequest(url, handleArtistsResponse);
};

const handleArtistsResponse = (response) => {
  artistTableBody.innerHTML = "";
  response.data.forEach((artist) => {
    const tr = `<tr>
                        <td class="p-4 border-b border-slate-200">
                            <div class="flex items-center gap-3">
                                <img src="${
                                  artist.image || "/static/img/profile.jpg"
                                }"
                                    alt="${artist}"
                                    class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                                <div class="flex flex-col">
                                    <p class="text-sm font-semibold text-white">
                                        ${artist.name}
                                    </p>
                                </div>
                            </div>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm font-semibold text-white">
                                ${artist.albums} Albums
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm font-semibold text-white">
                               ${artist.tracks} Tracks
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm text-white">
                                ${artist.popularity} Fans
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <button onclick="artistPlayer(this)" class="btn btn-sm btn-success btn-circle" id="play-artist-${
                              artist.id
                            }">
                                <i class="fa fa-play"></i>
                            </button>
                        </td>
                    </tr>`;
    artistTableBody.innerHTML += tr;
  });
};

fetchArtists(`/creator/artist-response/`);
