package handlers

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func GetUserByMail(c *gin.Context) {
	mail := c.Param("mail")

	c.JSON(http.StatusOK, gin.H{
		"value": mail,
	})
}

func GetUserById(c *gin.Context) {
	id := c.Param("id")
	c.JSON(http.StatusOK, gin.H{
		"value": id,
	})
}
