package com.example.localdb



import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.lifecycle.lifecycleScope
import com.example.localdb.database.AppDatabase
import com.example.localdb.database.User
import kotlinx.coroutines.launch

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        //Get the Database Instance
        val db = AppDatabase.getDatabase(this)

        // Access the DAO(data access object)
        val userDao = db.userDao()

        setContent {
            var name by remember { mutableStateOf("") }
            var email by remember { mutableStateOf("") }

            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(16.dp),
                verticalArrangement = Arrangement.Center
            ) {
                OutlinedTextField(
                    value = name,
                    onValueChange = { name = it },
                    label = { Text("Name") },
                    modifier = Modifier.fillMaxWidth()
                )

                Spacer(modifier = Modifier.height(8.dp))

                OutlinedTextField(
                    value = email,
                    onValueChange = { email = it },
                    label = { Text("Email") },
                    modifier = Modifier.fillMaxWidth()
                )

                Spacer(modifier = Modifier.height(16.dp))

                Button(
                    onClick = {
                        // Save data in background
                        lifecycleScope.launch {
                            val user = User(name = name, email = email)

                            // Insert user into the database
                            userDao.insertUser(user)
                        }
                    },
                    modifier = Modifier.fillMaxWidth()
                ) {
                    Text("Save to Database")
                }
            }
        }
    }
}



// In this file only write this code in the exam

//In the on create function

//val db = AppDatabase.getDatabase(this)
//val userDao = db.userDao()
//
//// Inside Button onClick
//lifecycleScope.launch {
//    val user = User(name = name, email = email)
//    userDao.insertUser(user)
//}




