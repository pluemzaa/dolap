<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flow2"/>
        <attribute name="authors" value="choco"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-18 01:19:08 AM"/>
        <attribute name="created" value="Y2hvY287REVTS1RPUC1QTVZSRjk5OzIwMjUtMDctMTg7MDE6MTI6NDggQU07Mjg4Ng=="/>
        <attribute name="edited" value="Y2hvY287REVTS1RPUC1QTVZSRjk5OzIwMjUtMDctMTg7MDE6MTk6MDggQU07MjsyOTk4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="m, inter" type="Real" array="False" size=""/>
            <declare name="y, i" type="Integer" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="inter"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="y"/>
            <while expression="i &lt; y">
                <assign variable="m" expression="m*(1+inter/100)"/>
                <output expression="&quot;Year&quot; &amp; (i+1) &amp; &quot;:&quot; &amp; m" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>