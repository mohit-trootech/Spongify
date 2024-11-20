/**Music App JavaScripts */

const albumChange = (elem) => {
  const url = list_albums_urls + "?q=" + elem.value;
  albums_list(url);
};

const findArtistHandle = (elem) => {
  const url = find_artists_url + "?q=" + elem.value;
  find_artists(url);
};

const albums_list = async (url) => {
  await getRequest(url, updateAlbumOptions);
};

const find_artists = async (url) => {
  await getRequest(url, updateArtistsOptions);
};

const updateAlbumOptions = (response) => {
  /**Update Album Options Handling */
  const dataList = document.querySelector("datalist#albums_lists");
  // First Clear All Options
  dataList.innerHTML = "";
  response.items.forEach((element) => {
    const option = document.createElement("option");
    //   value is ID & name is Text
    option.value = element.id;
    option.textContent = element.name;
    dataList.appendChild(option);
  });
};

const updateArtistsOptions = (response) => {
  /**Update Artists Option Handling */
  const select = document.querySelector("select#id_for_artists");
  // Clear Options Other Then Selected
  let optionsSelected = $("select#id_for_artists option:selected");
  let optionsAvailable = $("select#id_for_artists option");
  optionsAvailable.each(function () {
    if (!$(this).is(optionsSelected)) {
      $(this).remove();
    }
  });

  response.items.forEach((element) => {
    const option = document.createElement("option");
    //   value is ID & name is Text
    option.value = element.id;
    option.textContent = element.name;
    select.appendChild(option);
  });
};

albums_list(list_albums_urls);
find_artists(find_artists_url);
