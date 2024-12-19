package routes

import (
	"github.com/gin-gonic/gin"
	"my_bookshop/handlers"
)

func UserRoutes(router *gin.Engine) {
	userRoutes := router.Group("/user")
	{
		userRoutes.GET("/:mail", handlers.GetUserByMail)
		userRoutes.GET("/:id", handlers.GetUserById)
	}
}
