<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="4"/>
        <attribute name="authors" value="User"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 12:08:12 AM"/>
        <attribute name="created" value="VXNlcjtERVNLVE9QLUFPVUoxTUc7MjAyNS0wNy0xNjsxMTozMzoyMCBQTTsyNzc1"/>
        <attribute name="edited" value="VXNlcjtERVNLVE9QLUFPVUoxTUc7MjAyNS0wNy0xNzsxMjowODoxMiBBTTs0OzI4NzY="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="money, interest, acc" type="Real" array="False" size=""/>
            <declare name="years, year" type="Integer" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="money"/>
            <output expression="&quot;Input interest(%):&quot;" newline="True"/>
            <input variable="interest"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="years"/>
            <assign variable="acc" expression="money"/>
            <for variable="year" start="1" end="years" direction="inc" step="1">
                <assign variable="acc" expression="acc * ( 1 + (interest/100) )"/>
                <output expression="&quot;Year &quot;&amp;year&amp;&quot; : &quot;&amp;acc" newline="True"/>
            </for>
        </body>
    </function>
</flowgorithm>