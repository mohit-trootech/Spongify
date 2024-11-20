/**Common Axios Request */

const getRequest = async (url, callback) => {
  /**Common Axios Get Request */
  await axiosRequest("GET", url, null, callback);
};

const postRequest = async (url, data, callback) => {
  /**Common Axios Post Request */
  await axiosRequest("POST", url, data, callback);
};

const axiosRequest = async (method, url, data, callback) => {
  try {
    let response = await axios({
      method: method,
      url: url,
      data: data,
    });
    if (callback) {
      callback(response.data);
    }
    return response;
  } catch (error) {
    console.error(error);
  }
};
