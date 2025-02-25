/**Common Constants */
// Urls Constants
const list_albums_urls = "/creator/albums_list/";
const find_artists_url = "/creator/find_artists/";
let albumTableBody = null;
let artistTableBody = null;
let timer = null;
let currentPlaylistTableBody = null;
const audio = new Audio();
audio.controls = true;
let audioSrc = null;
let songs = null;
let current = null;
let mapIds = {};
let playerUpdate = null;
let toast = null;
let toastBody = null;
