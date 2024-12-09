import axios from "redaxios";
import { api } from "./api.js";

export async function find_user(mail) {
  const res = await axios.get(`${api.back_api}/user/${mail}`);
  return res.data.user_info;
}

export async function create_user(fname, lname, mail, password, newsletter) {
  const res = await axios.post(`${api.back_api}/api/user`, {
    fname: fname,
    lname: lname,
    mail: mail,
    password: password,
    newsletter: newsletter,
  });
  return res.data;
}

export async function connect_user(mail, password) {
  const res = await axios.post(`${api.back_api}/api/auth/login`, {
    mail: mail,
    password: password,
  });
  return res.data;
}
