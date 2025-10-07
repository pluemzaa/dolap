<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Problems _1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:59:52 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDE6NTc6NDEgUE07MjU3OQ=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6NTk6NTIgUE07MTA7Mjc0MA=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="childprice, adultprice, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <assign variable="childprice" expression="120"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <assign variable="adultprice" expression="189"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="childprice"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adultprice"/>
            <assign variable="total" expression="(childprice*120)+(adultprice*189)"/>
            <output expression="&quot;You ordered &quot; &amp;childprice&amp; &quot; children and &quot; &amp;adultprice&amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp;total&amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>