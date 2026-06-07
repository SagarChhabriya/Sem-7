package com.example.localdb.database


import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query


//This part defines how you interact with the database.
// Here, we provide functions to insert data and fetch data.
@Dao
interface UserDao {

    //suspend function used to run this in background
    @Insert
    suspend fun insertUser(user: User)       // Insert a user into the table

}


//write this full in paper