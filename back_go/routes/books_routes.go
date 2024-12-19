package routes

import (
	"github.com/gin-gonic/gin"
	"my_bookshop/handlers"
)

func BookRoutes(router *gin.Engine) {
	bookRoutes := router.Group("/books")
	{
		bookRoutes.GET("/", handlers.GetAllBooks)
	}
}
