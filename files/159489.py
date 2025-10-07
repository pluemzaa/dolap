<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="ex4"/>
        <attribute name="authors" value="MY COM"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-23 08:45:31 PM"/>
        <attribute name="created" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE2OzExOjQwOjQwIFBNOzI3NTQ="/>
        <attribute name="edited" value="TVkgQ09NO0RFU0tUT1AtSEk5QUUwTTsyNTY4LTA3LTE3OzEyOjA1OjI5IEFNOzI7Mjg1OA=="/>
        <attribute name="edited" value="cG9vcmk7UE9PUklQQVQ7MjAyNS0wNy0yMzswODo0NTozMSBQTTsxOzI1Njk="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="mon, Ser, mon1, mon2, mon3, ser1" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="mon"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="ser"/>
            <assign variable="ser1" expression="ser*1/100"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i &lt;= year">
                <assign variable="mon" expression="mon*(1+ser/100)"/>
                <output expression="&quot;year &quot;&amp;i&amp;&quot;:&quot;&amp;mon" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>