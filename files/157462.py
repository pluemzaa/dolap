<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="683380460-1"/>
        <attribute name="authors" value="acer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-19 03:21:57 PM"/>
        <attribute name="created" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0xOTswMjowOTozNiBQTTsyNzQ3"/>
        <attribute name="edited" value="YWNlcjtMQVBUT1AtNzFQQ09EM0w7MjU2OC0wNy0xOTswMzoyMTo1NyBQTTsxOzI4NTM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="childPrice, adultPrice, numChildren, numAdults, total" type="Integer" array="False" size=""/>
            <assign variable="childPrice" expression="120"/>
            <assign variable="adultPrice" expression="189"/>
            <assign variable="total" expression="0"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="numChildren"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="numAdults"/>
            <assign variable="total" expression="(numChildren*120)+(numAdults*189)"/>
            <output expression="&quot;You ordered &quot; &amp; numChildren &amp; &quot; children and &quot; &amp; numAdults &amp; &quot; adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>