<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="folw4.fl"/>
        <attribute name="authors" value="laila"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-22 09:55:27 PM"/>
        <attribute name="created" value="bGFpbGE7VEFUVEVQOzIwMjUtMDctMjE7MDY6MTE6NTggUE07MjI2NQ=="/>
        <attribute name="edited" value="bGFpbGE7VEFUVEVQOzIwMjUtMDctMjI7MDk6NTU6MjcgUE07MTsyMzgx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest" type="Real" array="False" size=""/>
            <declare name="years, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="years"/>
            <while expression="i&lt;years">
                <assign variable="money" expression="money*(1+interest/100)"/>
                <output expression="&quot;Year&quot;&amp;(i+1)&amp;&quot;:&quot;&amp;money" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>