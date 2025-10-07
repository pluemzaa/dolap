<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4_4"/>
        <attribute name="authors" value="ASUS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 03:45:26 PM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtN1FTMjkyOUE7MjU2OC0wNy0xNjswMzozMToxOSBQTTsyNjE5"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtN1FTMjkyOUE7MjU2OC0wNy0xNjswMzo0NToyNiBQTTs1OzI3MzQ="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="year, i, years" type="Integer" array="False" size=""/>
            <declare name="money, inst" type="Real" array="False" size=""/>
            <assign variable="i" expression="0"/>
            <output expression="&quot;Input money: &quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%): &quot;" newline="True"/>
            <input variable="inst"/>
            <output expression="&quot;Input years: &quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="years" expression="1"/>
            <while expression="year &gt; i">
                <output expression="&quot;Year &quot; &amp;years&amp; &quot;: &quot;" newline="False"/>
                <assign variable="years" expression="years + 1"/>
                <assign variable="money" expression="money * (1+(inst/100))"/>
                <assign variable="i" expression="i+1"/>
                <output expression="money" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>