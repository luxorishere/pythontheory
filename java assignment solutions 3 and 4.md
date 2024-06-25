### Assignment-3

1. **Significance of Functional Interface in Java**:
   Functional interfaces in Java are single abstract method interfaces, which facilitate the use of lambda expressions and method references, enabling functional programming in Java.
   ```java
   @FunctionalInterface
   interface MyFunctionalInterface {
       void execute();
   }
   ```

2. **Lambda Expressions with Example**:
   Lambda expressions provide a clear and concise way to represent an anonymous function, making code more readable and concise.
   ```java
   MyFunctionalInterface func = () -> System.out.println("Hello, World!");
   func.execute();
   ```

3. **64 Encode and Decode (Program)**:
   Base64 encoding converts binary data to a text format, while decoding reverses this process.
   ```java
   String encoded = Base64.getEncoder().encodeToString("example".getBytes());
   String decoded = new String(Base64.getDecoder().decode(encoded));
   ```

4. **Switch Expression: yield Keyword**:
   The `yield` keyword in a switch expression returns a value from a case branch, enhancing switch expressions.
   ```java
   int result = switch (day) {
       case MONDAY -> 1;
       case TUESDAY -> { yield 2; }
       default -> 0;
   };
   ```

5. **Type Annotation and Repeating Annotation**:
   Type annotations can be used to annotate types, while repeating annotations allow the same annotation to be used multiple times.
   ```java
   @Target(ElementType.TYPE_USE)
   @interface NonNull {}
   
   @Repeatable(Schedules.class)
   @interface Schedule { String day(); }
   ```

6. **Try with Resource Example**:
   The try-with-resources statement ensures that each resource is closed at the end of the statement.
   ```java
   try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
       System.out.println(br.readLine());
   } catch (IOException e) {
       e.printStackTrace();
   }
   ```

### Assignment-4

1. **Collection Framework Hierarchy**:
   The Collection framework provides a standard way to handle groups of objects, including interfaces like List, Set, and Map.
   ```java
   List<String> list = new ArrayList<>();
   ```

2. **Queue Interface Implementation**:
   The Queue interface represents a collection designed for holding elements prior to processing.
   ```java
   Queue<Integer> queue = new LinkedList<>();
   queue.add(1);
   queue.add(2);
   System.out.println(queue.poll());
   ```

3. **HashMap and LinkedHashMap Class**:
   HashMap is a hash table-based implementation, while LinkedHashMap maintains a doubly-linked list of its entries for predictable iteration order.
   ```java
   HashMap<Integer, String> hashMap = new HashMap<>();
   LinkedHashMap<Integer, String> linkedHashMap = new LinkedHashMap<>();
   ```

4. **Iterator Interface and Collection Interface**:
   The Iterator interface provides methods to iterate over a collection, while the Collection interface is the root interface for Java collections.
   ```java
   Iterator<String> iterator = list.iterator();
   while (iterator.hasNext()) {
       System.out.println(iterator.next());
   }
   ```

5. **Comparable vs Comparator Interface**:
   Comparable is used for natural ordering of objects, while Comparator is used for custom ordering.
   ```java
   class Person implements Comparable<Person> {
       String name;
       public int compareTo(Person other) {
           return this.name.compareTo(other.name);
       }
   }

   Comparator<Person> byName = (Person p1, Person p2) -> p1.name.compareTo(p2.name);
   ```