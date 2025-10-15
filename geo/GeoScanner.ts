import axios from "axios";

export class GeoScanner {
  async getGeoLocation(ip: string) {
    // Free API: ipapi.com, ipinfo.io
    const url = `https://ipapi.co/${ip}/json/`;
    try {
      const res = await axios.get(url);
      return {
        ip,
        city: res.data.city,
        country: res.data.country_name,
        org: res.data.org
      };
    } catch (err) {
      return { ip, error: "Geo lookup failed" };
    }
  }
}
