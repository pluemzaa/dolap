<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab4"/>
        <attribute name="authors" value="ASUS"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 12:23:27 AM"/>
        <attribute name="created" value="QVNVUztMQVBUT1AtVEtNRTJEN0E7MjU2OC0wNy0yMDswNDoyMTo1NCBQTTsyNjU4"/>
        <attribute name="edited" value="QVNVUztMQVBUT1AtVEtNRTJEN0E7MjU2OC0wNy0yMTsxMjoyMzoyNyBBTTsxOzI3NTM="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, total, interest" type="Real" array="False" size=""/>
            <declare name="year, i" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="year"/>
            <assign variable="total" expression="money"/>
            <assign variable="i" expression="1"/>
            <while expression="i&lt;=year">
                <assign variable="total" expression="total*(1+interest/100)"/>
                <output expression="&quot;Year&quot;&amp;&quot; &quot;&amp;i&amp;&quot;:&quot;&amp;total" newline="True"/>
                <assign variable="i" expression="i+1"/>
            </while>
        </body>
    </function>
</flowgorithm>