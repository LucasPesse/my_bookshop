package main

import (
	"github.com/gin-gonic/gin"
	"my_bookshop/db"
	"my_bookshop/routes"
)

func main() {
	db.ConnectDB()

	r := gin.Default()

	routes.BookRoutes(r)

	r.Run(":8080")
}
