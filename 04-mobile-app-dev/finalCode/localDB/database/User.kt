package com.example.localdb.database

//This part defines the structure of your data in the SQLite database.
// Use the @Entity annotation to mark the class as a table.
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "user_table")
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,           // Auto-generated unique ID
    val name: String,                                    // Name of the user
    val email: String                                    // Email of the user

)

//write fulll code in exam