<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="i hate nnja"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 05:03:28 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDM6NTU6NDggUE07MjU4Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6MDM6MjggUE07MTY7Mjc0MQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="childPrice, adultPrice, total" type="Integer" array="False" size=""/>
            <assign variable="childPrice" expression="120"/>
            <assign variable="adultPrice" expression="189"/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="childPrice"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adultPrice"/>
            <output expression="&quot;You ordered&quot;&amp;childPrice&amp;&quot;childrenand&quot;&amp;adultPrice&amp;&quot;adults&quot;" newline="True"/>
            <output expression="&quot;Total price: &quot;&amp;(childPrice*120)+(adultPrice*189) &amp;&quot; Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>