import axios from "redaxios";

export async function get_books() {
  const res = await axios.get("http://127.0.0.1:5000/books");
  return res.data;
}

export async function get_a_book(id) {
  const res = await axios.get(
    `https://www.googleapis.com/books/v1/volumes/${id}`,
  );
  return res.data;
}
