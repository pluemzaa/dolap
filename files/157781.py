<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="w4"/>
        <attribute name="authors" value="staff"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-21 01:29:23 PM"/>
        <attribute name="created" value="c3RhZmY7REVTS1RPUC1NNDUwQ002OzIwMjUtMDctMTk7MTI6MzM6MDIgUE07MjgyNA=="/>
        <attribute name="edited" value="c3RhZmY7REVTS1RPUC1NNDUwQ002OzIwMjUtMDctMjE7MDE6Mjk6MjMgUE07MjsyOTMy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money" type="Real" array="False" size=""/>
            <declare name="Allyears, years, interest" type="Integer" array="False" size=""/>
            <assign variable="years" expression="1"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="Allyears"/>
            <while expression="years &lt;= Allyears">
                <assign variable="money" expression="(money*(interest/100))+money"/>
                <output expression="&quot;Year&quot; &amp;years&amp; &quot;:&quot; &amp;money" newline="True"/>
                <assign variable="years" expression="years + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>