/**Spongify UI Utilities Javascripts */

const durationReadbleFormat = (duration) => {
  /**Convert Duration from Seconds to Readable Format */

  if (duration) {
    const hrs = ~~(duration / 3600);
    const mins = ~~((duration % 3600) / 60);
    const secs = ~~duration % 60;

    let ret = "";

    if (hrs > 0) {
      ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
    }

    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
  } else {
    return "00:00";
  }
};
