import * as Books from "$/lib/books.js";

export async function load() {
  return await Books.get_books();
}
