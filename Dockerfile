# Step 1: Build and package the code into a runnable .jar file
FROM maven AS builder

WORKDIR /build
COPY pom.xml .

COPY . .
RUN mvn package

# Step 2: Transfer the jar file 
# along with the Lucene index to the new 
# image from which the final container will be built
FROM openjdk:17

COPY --from=builder /build/target/qa-app-0.0.1-SNAPSHOT.jar app.jar

COPY questions_index/ questions_index/

ENTRYPOINT ["java", "-jar", "/app.jar"]


