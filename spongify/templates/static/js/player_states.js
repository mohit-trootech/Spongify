/**Load Dynamic Ajax Data to Datatables */
let currentPlaylistTableBody = null;
const audio = new Audio();
audio.controls = true;
let audioSrc = null;
let songs = null;
let current = null;
let mapIds = {};
let playerUpdate = null;
const handleCurrentPlaylist = () => {
  currentPlaylistTableBody = document.getElementById(
    "current-playlist-table-body"
  );
  for (let i = 0; i < songs.length; i++) {
    let track = songs[i];
    const tr = `<tr>
                        <td class="p-4 border-b border-slate-200">
                            <div class="flex items-center gap-3">
                                <img src="${
                                  track.image || "/static/img/profile.jpg"
                                }"
                                    alt="${track}"
                                    class="relative inline-block h-9 w-9 !rounded-full object-cover object-center" />
                                <div class="flex flex-col">
                                    <p class="text-sm font-semibold text-white">
                                        ${track.title}
                                    </p>
                                </div>
                            </div>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm font-semibold text-white truncate">
                                ${track.artists}
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm font-semibold text-white">
                               ${durationReadbleFormat(track.duration)}
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <p class="text-sm text-white">
                                ${track.popularity} Like
                            </p>
                        </td>
                        <td class="p-4 border-b border-slate-200">
                            <button onclick="trackPlayer(this)"  class="btn btn-sm btn-success btn-circle" id="play-track-${
                              track.id
                            }">
                                <i class="fa fa-play"></i>
                            </button>
                        </td>
                    </tr>`;
    currentPlaylistTableBody.innerHTML += tr;
  }
};
const setMapIds = (data) => {
  for (let i = 0; i < data.length; i++) {
    mapIds[data.id] = i;
  }
};
const updatePlayerDetails = () => {
  //document.getElementById("player-image").innerHTML = current.file;
  const titles = document.getElementsByClassName("player-title");
  const artists = document.getElementsByClassName("player-artist");
  for (let i = 0; i < titles.length; i++) {
    titles[i].innerText = current.title;
    artists[i].innerText = current.genre;
  }
};
const setAudioSrc = (data) => {
  audioSrc = data;
  //   updatePlayerProgress();
};
const setSongs = (data) => {
  songs = data;
};
const setCurrent = (data) => {
  current = data;
};
playerUpdate = (data) => {
  try {
    setMapIds(data);
    setSongs(data.data);
    setCurrent(songs[0]);
  } catch (error) {
    setMapIds(data);
    setSongs(data);
    setCurrent(songs);
  }
  setAudioSrc(current.file);
  audio.src = audioSrc;
  audio.play();
  audio.onended = () => {
    if (mapIds[current.id] + 1 < songs.length) {
      setCurrent(songs[mapIds[current.id] + 1]);
      setAudioSrc(current.file);
      audio.src = audioSrc;
      audio.play();
    } else {
      fetchRandomTracks();
    }
  };
  updatePlayerDetails();
  handleCurrentPlaylist();
  updatePlayerProgress();
};
const nextSong = () => {
  if (mapIds[current.id] + 1 < songs.length) {
    setCurrent(songs[mapIds[current.id] + 1]);
    setAudioSrc(current.file);
    audio.src = audioSrc;
    audio.play();
    updatePlayerDetails();
    updatePlayerProgress();
  } else {
    setCurrent(songs[0]);
    setAudioSrc(current.file);
    audio.src = audioSrc;
    audio.play();
    updatePlayerDetails();
    updatePlayerProgress();
  }
};
const prevSong = () => {
  if (mapIds[current.id] - 1 > 0) {
    setCurrent(songs[mapIds[current.id] - 1]);
    setAudioSrc(current.file);
    audio.src = audioSrc;
    audio.play();
    updatePlayerDetails();
  } else {
    setCurrent(songs[songs.length - 1]);
    setAudioSrc(current.file);
    audio.src = audioSrc;
    audio.play();
    updatePlayerDetails();
    updatePlayerProgress();
  }
};
const playPause = (elem) => {
  /**Play Pause Song if Audio Src Available*/
  if (audio.paused) {
    audio.play();
    elem.tagName === "I"
      ? elem.classList.replace("fa-play", "fa-pause")
      : elem.children[0].classList.replace("fa-play", "fa-pause");
  } else {
    audio.pause();
    elem.tagName === "I"
      ? elem.classList.replace("fa-pause", "fa-play")
      : elem.children[0].classList.replace("fa-pause", "fa-play");
  }
};

const playNewSong = () => {
  /**Play Current Song */
  audio.src = audioSrc;
  audio.play();
  document.getElementById("play-pause").innerHTML =
    '<i className="fa fa-pause"></i>';
  updatePlayerDetails();
  updatePlayerProgress();
};

const updatePlayerProgress = () => {
  const progress = document.getElementsByClassName("player-progress");
  const currentDuration = document.getElementsByClassName("current-progress");
  const songDuration = document.getElementsByClassName("song-progress");
  songDuration[0].innerText = durationReadbleFormat(current.duration);
  songDuration[1].innerText = durationReadbleFormat(current.duration);
  /**Audio on Time Update is Not a Function */
  progress[0].max = current.duration;
  progress[1].max = current.duration;
  audio.ontimeupdate = () => {
    progress[0].value = audio.currentTime;
    progress[1].value = audio.currentTime;
    currentDuration[0].innerText = durationReadbleFormat(audio.currentTime);
    currentDuration[1].innerText = durationReadbleFormat(audio.currentTime);
  };
};
const repeatSong = (elem) => {
  elem.classList.toggle("btn-active");
  audio.loop = !audio.loop;
};

/**Update Music Player*/
const artistPlayer = async (elem) => {
  const id = elem.id.split("-")[2];
  if (!isNaN(Number(id))) {
    getRequest(`/creator/artist-tracks-response/${id}`, playerUpdate);
  }
};
const albumPlayer = async (elem) => {
  const id = elem.id.split("-")[2];
  if (!isNaN(Number(id))) {
    getRequest(`/creator/album-tracks-response/${id}`, playerUpdate);
  }
};
/**Track Player */
const trackPlayer = async (elem) => {
  const id = elem.id.split("-")[2];
  if (!isNaN(Number(id))) {
    getRequest(`/creator/tracks-api-response/${id}`, playerUpdate);
  }
};

const fetchRandomTracks = async () => {
  await getRequest("/creator/tracks-response/", playerUpdate);
};
