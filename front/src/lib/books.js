import axios from "redaxios";
import { api } from "./api.js";

export async function get_books() {
  const res = await axios.get(`${api.back_api}/books`);
  return res.data;
}

export async function get_a_book(id) {
  const res = await axios.get(`${api.book_api}/${id}`);
  return res.data;
}
