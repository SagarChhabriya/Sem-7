### Final Topics
- Android Networking
    - Retrofit2 plugins
    - Self reading: Managment


### Assignment: State Management
- Need
- Mutable with code
- State Hosting with 
- View model and LiveData Integration with code in detail





## Android Basics

**Huawei vs Google**

**Smart Phone**

To Remind: Dalvik VM

Launcher Changable Applications


### Android Runtime
- Dalvik VM
    - Dex Files (.class)
    - Compact and efficient than class files
    - Limited memeory and battery power
- Core Libraries
    - Java 5 Std edition
    - Collections, I/O etc...

### Application Framework
- API Interface
- Activity Manager - manages application life cycle
    - Sign (in/out), etc

- built in and user apps
- can replace built in apps


### Application Building Blocks
1. Activity: Each screen in your application
2. IntentReceiver: Just Once, Always
3. Service (location, GPS): Long Running Task
4. ContentProvider

Short Running and Long Running Task.



### Activities
Typically correspond to one UI Screen
- But, they can:
    - Be faceless
    - Be in a floating window
    - Return a value

### IntentReceivers
- Components that reponsd to broadcast 'intents'
- Way to respond to external notification or alarms
- Apps can invent and broadcast their own 


### Intents
- Think of intents as a verb and object; a description of what you want done
    - E.g., VIEW, CALL, PLAY, etc.
- System matches intent with with activity that can best provide the service
- Activities and IntentReceivers describe what intent they can service

### Services
- Faceless components that run in the background
    - E.g., Music player, network download, etc


### Content Providers
- Enables sharing of data across **applications**
    - e.g., address book, photo gallery

- Provides uniform APIs for:
    - querying
    - delete, update, and insert
- Content is represented by URI and MIME type


## Development Tools



- OnCreate(): overiddend method



# Week 2: Layouts

## Constraint Layout in Android

> Why Flat view hierarchy is important? + Constraint Layout Attributes| Exam


## Important Attributes

## Implementation Steps
1. Create a new project
2.
3.
4.


## Tyeps of Constraint Layous
- Relative Positioning
- Margins
- Bias
- Chains
- Guidelines
- Barriers (dynamic alignment)

## Features | Exam
- Flat View Hieratchy
- Aspect Ratio
- Chains and Barriers
- Guidelines
- Responsive UI Designs


## Advantages
- Drag and drop ui design
- Improved performance
- Easier animation integration
- Efficient layout calculation
- Supports complex UI designs

## Disadvantages
- Complex XML Code
- Design editor may not match runtime UI
- Requires proper constraints for correct layout
- Seperate layout files may be needed for landscape mode



### Internationlisation
RTL | LTR: Right to left, left to right
- English, Urdu, Sindhi responsive UI



## Comparision with Other Layouts
- LinearLayout
- RelativeLayout
- GridLayout
- ConstraintLayout


## Lab
1. Create a new project in Android Studio (Empty Activity)
2. Add dependency: Implementation android.constraintlayout:constraintlayout:2.2.0
3. Use constrain layout

### DPI
dot per inches


### Exam: 
Java> com.example.application > new activity > Basic
You can change the name of an activity <br>

- Activity Name: CamelCase, no spaces
- Layout Name: snake case
- Launcher Activity: Like landing page






### Sep 26 Mad
Composable function, preview function, up to 9 Lazy list
Columns and Row should be inside Composable
https://www.geeksforgeeks.org/android/basics-of-jetpack-compose-in-android/
https://www.geeksforgeeks.org/android/text-in-android-using-jetpack-compose/ 
	MainActivity.kt
https://www.geeksforgeeks.org/android/button-in-android-using-jetpack-compose/

Creation of Jetpack project


---

## After MID

### Nov 07

TODO: Chapter 5 of Book

### Nov 14
- Firebase Auth
- Kotlin Coroutines

https://www.geeksforgeeks.org/android/kotlin-coroutines-on-android/

Remember 

dependencies {
  implementation ("org.jetbrains.kotlinx:kotlinx-coroutines-core:x.x.x")
  implementation ("org.jetbrains.kotlinx:kotlinx-coroutines-android:x.x.x")
}