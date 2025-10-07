<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4"/>
        <attribute name="authors" value="charp"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 07:22:24 PM"/>
        <attribute name="created" value="Y2hhcnA7QVNVUzsyMDI1LTA3LTE2OzA2OjE1OjA1IFBNOzIxMjY="/>
        <attribute name="edited" value="Y2hhcnA7QVNVUzsyMDI1LTA3LTE2OzA3OjIyOjI0IFBNOzI7MjIzNQ=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, year, i" type="Integer" array="False" size=""/>
            <declare name="total" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <assign variable="total" expression="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <while expression="i&lt;year">
                <assign variable="total" expression="total*(1+interest/100)"/>
                <output expression="&quot;Year&quot; &amp; (i+1) &amp; &quot;:&quot; &amp; total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>