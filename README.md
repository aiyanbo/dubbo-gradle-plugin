# Dubbo Gradle Plugins

## dubbo-gradle-plugin

```kotlin
plugins {
    id("com.google.protobuf") version "0.8.17"
}

protobuf {

    protoc {
        artifact = if (osdetector.os == "osx") {
            "com.google.protobuf:protoc:3.21.2:osx-x86_64"
        } else {
            "com.google.protobuf:protoc:3.21.2"
        }
    }

    plugins {

        id("dubbo") {
            artifact = "org.jmotor.gradle:dubbo-gradle-plugin:1.0.0@jar"
        }
    }

    generateProtoTasks {
        ofSourceSet("main").forEach {
            it.plugins {
                id("dubbo")
            }
        }
    }
}
```


## dubbo-triple-gradle-plugin

```kotlin
plugins {
    id("com.google.protobuf") version "0.8.17"
}

protobuf {

    protoc {
        artifact = if (osdetector.os == "osx") {
            "com.google.protobuf:protoc:3.21.2:osx-x86_64"
        } else {
            "com.google.protobuf:protoc:3.21.2"
        }
    }

    plugins {

        id("dubbo-triple") {
            artifact = "org.jmotor.gradle:dubbo-triple-gradle-plugin:1.0.0@jar"
        }
    }

    generateProtoTasks {
        ofSourceSet("main").forEach {
            it.plugins {
                id("dubbo-triple")
            }
        }
    }
}
```


## dubbo-grpc-gradle-plugin


```kotlin
plugins {
    id("com.google.protobuf") version "0.8.17"
}

protobuf {

    protoc {
        artifact = if (osdetector.os == "osx") {
            "com.google.protobuf:protoc:3.21.2:osx-x86_64"
        } else {
            "com.google.protobuf:protoc:3.21.2"
        }
    }

    plugins {

        id("dubbo-grpc") {
            artifact = "org.jmotor.gradle:dubbo-grpc-gradle-plugin:1.0.0@jar"
        }

        id("grpc") {
            artifact = if (osdetector.os == "osx") {
                "io.grpc:protoc-gen-grpc-java:1.47.0:osx-x86_64"
            } else {
                "io.grpc:protoc-gen-grpc-java:1.47.0"
            }
        }
    }

    generateProtoTasks {
        ofSourceSet("main").forEach {
            it.plugins {
                id("grpc")
                id("dubbo-grpc")
            }
        }
    }
}
```
