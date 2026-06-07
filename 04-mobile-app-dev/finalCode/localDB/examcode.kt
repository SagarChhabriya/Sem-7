package com.example.localdb



import android.content.Context
import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.lifecycleScope
import androidx.room.*
import com.example.localdb.database.UserDao
import kotlinx.coroutines.launch



// ===== Entity (Table) =====
@Entity(tableName = "user_table")
data class User(
    @PrimaryKey(autoGenerate = true) val id: Int = 0,
    val name: String,
    val email: String
)

// ===== DAO (Data Access Object) =====
@Dao
interface UserDao {
    @Insert
    suspend fun insertUser(user: User)
}

// ===== Database =====
@Database(entities = [com.example.localdb.database.User::class], version = 1)
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


// ===== In MainActivity file =====

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Initialize the Room Database
    val db = AppDatabase.getDatabase(this)
    val userDao = db.userDao()

    //Inside the button
    lifecycleScope.launch {
        // Save user to database
        val user = User(name = name, email = email)
        userDao.insertUser(user)                 //insert data into database

    }

}



