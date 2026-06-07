package com.example.localdb.database


import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase
import android.content.Context


//This class is the main Room database instance.
// It uses the Singleton pattern to ensure only one instance of the database is created.

@Database(entities = [User::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao     // Get the DAO instance
    companion object {

        fun getDatabase(context: Context) = Room.databaseBuilder(
                context.applicationContext,
                AppDatabase::class.java,
                "user_database"               // Database name
            ).build()

    }
}

//write this full code in the paper